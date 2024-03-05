Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

function number_format(number, decimals, dec_point, thousands_sep) {
  // *     example: number_format(1234.56, 2, ',', ' ');
  // *     return: '1 234,56'
  number = (number + '').replace(',', '').replace(' ', '');
  var n = !isFinite(+number) ? 0 : +number,
    prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
    sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
    dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
    s = '',
    toFixedFix = function(n, prec) {
      var k = Math.pow(10, prec);
      return '' + Math.round(n * k) / k;
    };
  // Fix for IE parseFloat(0.55).toFixed(0) = 0;
  s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
  if (s[0].length > 3) {
    s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
  }
  if ((s[1] || '').length < prec) {
    s[1] = s[1] || '';
    s[1] += new Array(prec - s[1].length + 1).join('0');
  }
  return s.join(dec);
}
// Bar Chart Example
var ctx = document.getElementById("myBarChart");
var myBarChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ["2014년", "2015년", "2016년", "2017년", "2018년", "2019년", "2020년", "2021년", "2022년", "2023년", "2024년"],
    datasets: [{
      label: "ARIMA",
      lineTension: 0.3,
      backgroundColor: "rgba(78, 115, 223, 0.05)",
      borderColor: "rgba(78, 115, 223, 1)",
      pointRadius: 3,
      pointBackgroundColor: "rgba(78, 115, 223, 1)",
      pointBorderColor: "rgba(78, 115, 223, 1)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
      pointHoverBorderColor: "rgba(78, 115, 223, 1)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: [18688.0, 18738.5, 18284.5, 16601.0, 14717.5, 13444.5, 11915.5, 10671.5, 9632.4, 8408.5, 7153.7]
    }, {
      label: "SSM",
      lineTension: 0.3,
      backgroundColor: "rgba(255, 99, 132, 0.05)",
      borderColor: "rgba(255, 99, 132, 0.05)",
      pointRadius: 3,
      pointBackgroundColor: "rgba(255, 99, 132, 0.05)",
      pointBorderColor: "rgba(255, 99, 132, 0.05)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(255, 99, 132, 0.05)",
      pointHoverBorderColor: "rgba(255, 99, 132, 0.05)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: [18688.0, 18738.5, 18284.5, 16601.0, 14717.5, 13444.5, 11915.5, 10671.5, 10187.84, 8564.846, 7611.496]
    }, {
      label: "DLDA",
      lineTension: 0.3,
      backgroundColor: "rgba(54, 162, 235, 0.05)",
      borderColor: "rgba(54, 162, 235, 0.05)",
      pointRadius: 3,
      pointBackgroundColor: "rgba(54, 162, 235, 0.05)",
      pointBorderColor: "rgba(54, 162, 235, 0.05)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(54, 162, 235, 0.05)",
      pointHoverBorderColor: "rgba(54, 162, 235, 0.05)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: [18688.0, 18738.5, 18284.5, 16601.0, 14717.5, 13444.5, 11915.5, 10671.5, 9198.291, 8037.506, 7078.614]
    },
    ],
  },
  options: {
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: 10,
        right: 25,
        top: 25,
        bottom: 0
      }
    },
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false,
          drawBorder: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          maxTicksLimit: 5,
          padding: 10,
          callback: function(value, index, values) {
            return number_format(value);
          }
        },
        gridLines: {
          color: "rgb(234, 236, 244)",
          zeroLineColor: "rgb(234, 236, 244)",
          drawBorder: false,
          borderDash: [2],
          zeroLineBorderDash: [2]
        }
      }],
    },
    legend: {
      display: true
    },
  }
});