// Add a method to filter data for a specific area and within a month
filterDataForAreaAndMonth: function(data, area) {
    const currentDate = new Date();
    const oneMonthAgo = new Date();
    oneMonthAgo.setMonth(currentDate.getMonth() - 1);

    return data.filter(route => {
        // Filter by area
        if (route.title === area) {
            // Filter by timestamp within the last month
            return route.stations.some(station => {
                return station.machine_descriptors.some(descriptor => {
                    return descriptor.datapoints.some(dp => {
                        if (dp.timestamp) {
                            const dpTimestamp = new Date(dp.timestamp);
                            return dpTimestamp >= oneMonthAgo;
                        }
                        return false;
                    });
                });
            });
        }
        return false;
    });
},