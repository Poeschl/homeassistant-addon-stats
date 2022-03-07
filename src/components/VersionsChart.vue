<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title">Installations grouped by version</h5>
      <DoughnutChart :chart-data="this.getChartData()" :options="chartOptions"/>
    </div>
  </div>
</template>

<script>
import {DoughnutChart} from 'vue-chart-3';
import {Chart, registerables} from "chart.js";
import compareVersions from 'compare-versions';
import {interpolateTurbo} from "d3-scale-chromatic";

Chart.register(...registerables);

export default {
  name: "VersionsChart",
  props: ["versions"],
  components: {
    DoughnutChart
  },
  data() {
    return {
      chartOptions: {
        animation: false,
        borderColor: '#121213',
        plugins: {
          legend: {
            position: 'right'
          }
        }
      }
    }
  },
  methods: {
    getChartData() {
      const sortedVersions = Object.keys(this.versions).map((key) => {
        return [key, this.versions[key]]
      }).sort((first, second) => {
        return compareVersions(first[0], second[0])
      })

      const labels = []
      const values = []
      for (const versionData of sortedVersions) {
        labels.push(versionData[0])
        values.push(versionData[1])
      }
      const colors = this.generateColors(labels.length)

      return {
        labels: labels,
        datasets: [
          {
            backgroundColor: colors,
            data: values
          }
        ]
      }
    },
    generateColors(dataLength,) {
      const colorStart = 0.04
      const colorEnd = 1
      const colorRange = colorEnd - colorStart;
      const intervalSize = colorRange / dataLength;
      let colorPoint;
      const colorArray = [];

      for (let i = 0; i < dataLength; i++) {
        colorPoint = (colorStart + (i * intervalSize));
        colorArray.push(interpolateTurbo(colorPoint));
      }

      return colorArray;
    }
  }
}
</script>
