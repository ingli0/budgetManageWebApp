let myChart;
let chartType = 'bar'; // Default chart type

const renderChart = (data, labels, chartType) => {
    var ctx = document.getElementById('myChart').getContext('2d');
    if (myChart) {
        myChart.destroy();
    }
    myChart = new Chart(ctx, {
        type: chartType,
        data: {
            labels: labels,
            datasets: [{
                label: 'Sum',
                data: data,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

const getChartData = () => {
    fetch('/expense_category_summary')
        .then((res) => res.json())
        .then((results) => {
            const category_data = results.expense_category_data;
            const [labels, data] = [
                Object.keys(category_data),
                Object.values(category_data),
            ];

            renderChart(data, labels, chartType);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

const changeChartType = (type) => {
    chartType = type;
    getChartData();
}

document.addEventListener('DOMContentLoaded', () => {
    getChartData();
    
    setTimeout(() => {
        document.getElementById('myChart').style.height = '350px';
        document.getElementById('myChart').style.width = '350px';
    }, 100);
});
