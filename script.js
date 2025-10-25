document.getElementById('load-data-2013-btn').addEventListener('click', (e) => {
    e.preventDefault();
    loadChartData('data_2013.json', 'chart-container', 'Mesa', 'back-btn');
});

document.getElementById('load-data-2017-btn').addEventListener('click', (e) => {
    e.preventDefault();
    loadChartData('data_2017.json', 'chart-container', 'Mesa', 'back-btn');
});

document.getElementById('load-data-2021-btn').addEventListener('click', (e) => {
    e.preventDefault();
    loadChartData('data.json', 'chart-container', 'Mesa', 'back-btn');
});

document.getElementById('load-data-paso-2021-btn').addEventListener('click', (e) => {
    e.preventDefault();
    loadChartData('data_paso_2021.json', 'chart-container', 'Mesa', 'back-btn');
});

document.getElementById('load-data-2023-btn').addEventListener('click', (e) => {
    e.preventDefault();
    loadChartData('data_2023.json', 'chart-container', 'Mesa', 'back-btn');
});

document.getElementById('back-btn').addEventListener('click', () => {
    clearCharts('chart-container', 'back-btn');
});

document.getElementById('load-aggregated-data-btn').addEventListener('click', () => {
    fetch('aggregated_data.json')
        .then(response => response.json())
        .then(data => {
            const accordionContainer = document.getElementById('aggregated-data-container');
            accordionContainer.innerHTML = '';

            const desired_order = ["2013", "2017", "2021", "PASO 2021", "2023"];
            const all_years = [...new Set(Object.values(data).flatMap(mesa => Object.keys(mesa.years)))].sort((a, b) => {
                return desired_order.indexOf(a) - desired_order.indexOf(b);
            });

            for (const mesa_id in data) {
                const mesa_data = data[mesa_id];
                const total_votes = mesa_data.total_votes;
                const years_data = mesa_data.years;

                const accordionItem = document.createElement('div');
                accordionItem.classList.add('accordion-item');

                const accordionHeader = document.createElement('h2');
                accordionHeader.classList.add('accordion-header');
                accordionHeader.id = `heading-${mesa_id}`;

                const accordionButton = document.createElement('button');
                accordionButton.classList.add('accordion-button', 'collapsed');
                accordionButton.type = 'button';
                accordionButton.dataset.bsToggle = 'collapse';
                accordionButton.dataset.bsTarget = `#collapse-${mesa_id}`;
                accordionButton.ariaExpanded = 'false';
                accordionButton.ariaControls = `collapse-${mesa_id}`;
                
                if (mesa_id === '0') {
                    accordionButton.textContent = `Sumatoria Mesas 5 elecciones - Total Votos: ${total_votes}`;
                } else {
                    accordionButton.textContent = `Mesa ${mesa_id} - Total Votos: ${total_votes}`;
                }

                accordionHeader.appendChild(accordionButton);

                const accordionCollapse = document.createElement('div');
                accordionCollapse.id = `collapse-${mesa_id}`;
                accordionCollapse.classList.add('accordion-collapse', 'collapse');
                accordionCollapse.ariaLabelledby = `heading-${mesa_id}`;

                const accordionBody = document.createElement('div');
                accordionBody.classList.add('accordion-body');

                const canvas = document.createElement('canvas');
                accordionBody.appendChild(canvas);
                accordionCollapse.appendChild(accordionBody);

                accordionItem.appendChild(accordionHeader);
                accordionItem.appendChild(accordionCollapse);
                accordionContainer.appendChild(accordionItem);

                const parties = [...new Set(Object.values(years_data).flatMap(year => Object.keys(year)))];

                const datasets = parties.map(party => {
                    return {
                        label: party,
                        data: all_years.map(year => (years_data[year] && years_data[year][party]) || 0),
                        borderWidth: 1
                    }
                });

                new Chart(canvas, {
                    type: 'bar',
                    data: {
                        labels: all_years,
                        datasets: datasets
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });
            }
            document.getElementById('back-btn-aggregated').style.display = 'block';
        });
});

document.getElementById('back-btn-aggregated').addEventListener('click', () => {
    const accordionContainer = document.getElementById('aggregated-data-container');
    accordionContainer.innerHTML = '';
    document.getElementById('back-btn-aggregated').style.display = 'none';
});

function loadChartData(jsonFile, containerId, chartLabel, backButtonId) {
    fetch(jsonFile)
        .then(response => {
            if (!response.ok) {
                throw new Error("HTTP error " + response.status);
            }
            return response.json();
        })
        .then(data => {
            const chartContainer = document.getElementById(containerId);
            chartContainer.innerHTML = ''; // Clear previous charts

            for (const item in data) {
                const itemData = data[item];
                const canvasContainer = document.createElement('div');
                canvasContainer.classList.add('chart-container');
                const canvas = document.createElement('canvas');
                canvasContainer.appendChild(canvas);
                chartContainer.appendChild(canvasContainer);

                new Chart(canvas, {
                    type: 'bar',
                    data: {
                        labels: Object.keys(itemData),
                        datasets: [{
                            label: `${chartLabel} ${item}`,
                            data: Object.values(itemData),
                            backgroundColor: [
                                'rgba(255, 99, 132, 0.2)',
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 206, 86, 0.2)',
                                'rgba(75, 192, 192, 0.2)',
                                'rgba(153, 102, 255, 0.2)',
                                'rgba(255, 159, 64, 0.2)',
                                'rgba(255, 99, 132, 0.2)',
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 206, 86, 0.2)',
                            ],
                            borderColor: [
                                'rgba(255, 99, 132, 1)',
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 206, 86, 1)',
                                'rgba(75, 192, 192, 1)',
                                'rgba(153, 102, 255, 1)',
                                'rgba(255, 159, 64, 1)',
                                'rgba(255, 99, 132, 1)',
                                'rgba(54, 162, 23.5, 1)',
                                'rgba(255, 206, 86, 1)',
                            ],
                            borderWidth: 1
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            title: {
                                display: true,
                                text: `Resultados para ${chartLabel} ${item}`
                            }
                        },
                        scales: {
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });
            }
            document.getElementById(backButtonId).style.display = 'block'; // Show the back button
        })
        .catch(e => {
            console.error('Error al cargar los datos:', e);
            const chartContainer = document.getElementById(containerId);
            chartContainer.innerHTML = `<div class="alert alert-danger" role="alert">Error al cargar los datos. Por favor, asegúrese de que el archivo ${jsonFile} esté disponible y que la página se sirva a través de un servidor web.</div>`;
        });
}

function clearCharts(containerId, backButtonId) {
    const chartContainer = document.getElementById(containerId);
    chartContainer.innerHTML = '';
    document.getElementById(backButtonId).style.display = 'none'; // Hide the back button
}