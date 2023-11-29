    formatDataForGPT: function (routesData) {
        console.log(routesData);
        return {
            "routesData": routesData.map(route => {
                return {
                    if(route.title === 'LM-FULL'){
                        "Title": route.title,
                        "Stations": route.stations.map(station => {
                            return {
                                "Station": station.station,
                                "Machine Descriptors": station.machine_descriptors.map(descriptor => {
                                    return {
                                        "Full Station Name": descriptor.fullStationName,
                                        "Machine Descriptor": descriptor.machine_descriptor,
                                        "Data Points": descriptor.datapoints.map(dp => {
                                            return {
                                                "Timestamp": dp.timestamp,
                                                "Data": dp.data 
                                            };
                                        }),
                                    };
                                })
                            };
                        })
                    }
                };
            })
        };
    },   
