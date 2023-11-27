const UIService = {
    originalCameraTarget: null,
    originalCameraOrbit: null,

    // ... other properties and methods ...

    startupUI: function() {
        // ... other startup code ...

        // Initialize original camera position
        let modelViewer = document.querySelector("#model_viewer");
        UIService.originalCameraTarget = modelViewer.cameraTarget;
        UIService.originalCameraOrbit = modelViewer.cameraOrbit;
    },

    toggleStationLevel: function(parent_id) {
        let modelViewer = document.querySelector("#model_viewer");
        if($("#"+parent_id).hasClass("currentlyOpen")) {
            // Reset the camera position to original
            modelViewer.cameraTarget = UIService.originalCameraTarget;
            modelViewer.cameraOrbit = UIService.originalCameraOrbit;

            // ... rest of your existing code for handling currently open parent ...
        } else {
            // Change camera position for selected parent station
            modelViewer.cameraTarget = $("#" + parent_id).data("position");
            modelViewer.cameraOrbit = $("#" + parent_id).data("orbit");

            // ... rest of your existing code for handling not currently open parent ...
        }
    },

    // ... other methods ...
};