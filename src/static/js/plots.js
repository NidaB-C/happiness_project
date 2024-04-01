
Papa.parse('happiness_project/data/processed/cleaned_happiness_data.csv', {
    download: true,
    header: true,
    complete: function(results) {
        const data = results.data;

        // Initialize objects to hold total values and counts for averaging
        let totalsHappy = {}, totalsNotHappy = {}, countsHappy = {}, countsNotHappy = {};
        data.forEach(row => {
            const happinessIndicator = row['HappinessIndicator'];

            // Loop through each feature in the row
            for (const [key, value] of Object.entries(row)) {
                if (key !== 'HappinessIndicator') {
                    if (happinessIndicator == '1') {
                        totalsHappy[key] = (totalsHappy[key] || 0) + parseFloat(value);
                        countsHappy[key] = (countsHappy[key] || 0) + 1;
                    } else if (happinessIndicator == '0') {
                        totalsNotHappy[key] = (totalsNotHappy[key] || 0) + parseFloat(value);
                        countsNotHappy[key] = (countsNotHappy[key] || 0) + 1;
                    }
                }
            }
        });

        // Calculate averages
        let averagesHappy = {}, averagesNotHappy = {};
        for (const key of Object.keys(totalsHappy)) {
            averagesHappy[key] = totalsHappy[key] / countsHappy[key];
            averagesNotHappy[key] = totalsNotHappy[key] / countsNotHappy[key];
        }

        // Prepare data for Plotly
        const traceHappy = {
            x: Object.keys(averagesHappy),
            y: Object.values(averagesHappy),
            name: 'Happy',
            type: 'scatter'
        };

        const traceNotHappy = {
            x: Object.keys(averagesNotHappy),
            y: Object.values(averagesNotHappy),
            name: 'Not Happy',
            type: 'scatter'
        };

        const layout = {
            title: 'Average Feature Values Based on Happiness Indicator',
            xaxis: {
                title: 'Feature'
            },
            yaxis: {
                title: 'Average Value'
            }
        };

        Plotly.newPlot('plot', [traceHappy, traceNotHappy], layout);
    }
});
