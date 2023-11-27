const UIService = {

    startupUI: function() {
        UIService.parentStationClickHandler();
        UIService.showChildStation(false);
        UIService.toggleStationImageContainer(false);
        $("#mission_barchart").hide();
        $("#mission_overview").hide();
        UIService.updateCellDropdown();
        DataService.fetchRoutesData().then(() => {
            DataService.fetchLatestCellData().then(cellData => {
                const latestImageUrls = DataService.extractImageUrlsFromMissionData(cellData);
                ImageService.updateImageContainer('image_container', latestImageUrls);
            }).catch(error => {
                console.error("Failed to fetch latest cell data:", error);
            });
        }).catch(error => {
            console.error("Failed to fetch routes data:", error);
        });
    },

    parentStationClickHandler: function() {
        // Initialise the parent station click handler
        $(".parent_station").click(function() {
            UIService.toggleStationLevel($(this).attr("id"));

        })
    },

    showChildStation(show) {
        if(show == true) {
            $(".child_station").show();
            let modelViewer = document.querySelector("#model_viewer");
            modelViewer.cameraTarget = $("#" + stationName).data("position");
            modelViewer.cameraOrbit = $("#" + stationName).data("orbit");
        } else {
            $(".child_station").hide();
        }
    },

    updateCellDropdown: function() {
        DataService.fetchCells();
    },
    
    updateCellOverview: function() {
        $("#date_created").val(DataService.cellDateCreated);
        $("#last_run").val(DataService.cellLastRun);
        $("#duration").val(DataService.cellDuration);
        $("#inspections_num").val(DataService.cellNumInspections);
    },

    toggleStationImageContainer: function(show) {
        const stationImageContainer = document.getElementById("R698784236320332819");
        if (stationImageContainer) {
            stationImageContainer.style.display = show ? 'block' : 'none';
        } else {
            console.error("StationImageContainer not found");
        }
    },

    bindStationHotspots: function() {
        $(".station_hotspot").click(function () {
            UIService.selectStation($(this).attr("id"));
        });
    },

    toggleLatestImageContainer: function(show) {
        const stationImageContainer = document.getElementById("R698783736046332814");
        if (stationImageContainer) {
            stationImageContainer.style.display = show ? 'block' : 'none';
        } else {
            console.error("StationImageContainer not found");
        }
    },

    selectStation: async function(stationId) {
        console.log("Station selected:", stationId);
    
        try {
            const selectedStationData = await DataService.fetchStationMissionData(stationId);
    
            let allImageData = [];
    
            for (let descriptor of selectedStationData.machine_descriptors) {
                for (let missionFile of descriptor.missions) {
                    const missionData = await DataService.fetchMissionJson(missionFile);
    
                    const imageData = DataService.processMissionData(missionData)
                        .filter(item => item.url.includes(descriptor.fullStationName));
    
                    allImageData.push(...imageData);
                }
            }
            ImageService.updateImageContainer('station_image_container', allImageData);
            UIService.toggleStationImageContainer(true);
        } catch (error) {
            console.error("Error fetching data for station:", error);
        }
    },

    toggleStationLevel: function (
        parent_id) {
        if($("#"+parent_id).hasClass("currentlyOpen")) {
            console.log("parent station", parent_id)
            console.log(parent_id);
            $('#model_viewer').children('button').each(function () {
                if($(this).hasClass("station_hotspot") || $(this).hasClass("station_hotspot_hoverable")) {
                    if($(this).hasClass("child_station")) {
                        $(this).hide();
                    } else {
                        $(this).show();
                    }
                }
            });
    
            document.getElementById(parent_id).removeChild(document.getElementById(parent_id).lastChild);
            /*$("#"+parent_id).attr("data-childstations").split(",").forEach(station => {
                $("#"+station.replace(/ /g,'')).hide()
            }); */
            $("#"+parent_id).removeClass("currentlyOpen");
        } else {
            if($("#"+parent_id).attr("data-childstations").length > 1) {
                $('#model_viewer').children('button').each(function () {
                    if($(this).hasClass("station_hotspot") || $(this).hasClass("station_hotspot_hoverable")) {
                        if($(this).attr("id") != parent_id) {
                            // $(this).hide();
                        }
                    }
                });
                $("#"+parent_id).attr("data-childstations").split(",").forEach(station => {
                    $("#"+station.replace(/ /g,'')).show()
                });
    
                $("#"+parent_id).append('<span id="tempParentIcon" class="fa fa-sort-desc"></span>');
                $("#"+parent_id).addClass("currentlyOpen");
            }
        }
    },

    emptyModelViewerContainer: function(){
        $("#model_viewer_container").empty();
        console.log("modelviewercontainer emptied");
    },

    updateAreaDropdown: function(value) {
        $("#P18_AREA_DROPDOWN").val(value); // Change the model dropdown to show the current selected production line
    },

    showOverlay: function(show) {
        const overlay = document.getElementById("overlay_containerDEFAULT");
        if (overlay) { // Check if the overlay element exists
            if (show) {
                overlay.style.display = 'block';
            } else {
                overlay.style.display = 'none';
            }
        } else {
            console.error("Overlay container not found");
        }
    },    

    showBarChart: function(show) {
        const barChart = document.getElementById('mission_barchart');
        if (barChart) {
            barChart.style.display = show ? 'block' : 'none';
        } else {
            console.error("Bar chart container not found");
        }
    },    

    updateModelViewer: function(modelHTML) {
        const viewerContainer = document.getElementById('model_viewer_container');
        viewerContainer.innerHTML = modelHTML;
    },

};
