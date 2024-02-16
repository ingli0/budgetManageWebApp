import { Chart, Doughnut } from 'chart.js/auto';

// Define a function to render the chart
const renderChart = (data, labels) => {
    const ctx = document.getElementById('myChart');
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
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
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Expenses per Category'
                }
            }
        }
    });
}

// Define a function to fetch data and render the chart
const getChartData = () => {
    fetch('/expense_category_summary')
        .then(response => response.json())
        .then(data => {
            const categories = Object.keys(data.expense_category_data);
            const amounts = Object.values(data.expense_category_data);
            renderChart(amounts, categories);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

// Call the function to get data and render the chart when the DOM content is loaded
document.addEventListener('DOMContentLoaded', getChartData);
