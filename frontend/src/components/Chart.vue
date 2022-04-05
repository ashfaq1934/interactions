<template> 
  <div class="container">
    <div class="row">
      <div class="col">
    <div class="chart-wrapper">
      <apexchart 
      v-if="options.labels.length"
        width="800" type="donut" 
        :options="options" :series="series"
        @dataPointSelection="clickHandler">
      </apexchart>
    </div>
    </div>
    <div class="col">
      <table v-if="show" class="table">
        <thead>
          <tr>
            <th v-for="header in tableHeaders" v-bind:key="header">{{header}}</th>
          </tr>
      </thead>
      <tbody>
        <tr v-for="item in tableBody" v-bind:key="item">
          <td>{{item.sector_id}}</td>
          <td>{{item.sector_name}}</td>
          <td>{{item.sector_date}}</td>
        </tr>
      </tbody>
    </table>
    </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

 export default {
  name: 'Chart',
  data(){
    return{
      show: false,
      tableHeaders: ['Sector ID', 'Sector Name', 'Sector Date'],
      tableBody: [],
      interactions: [],
    options: {
      labels: [],
      events: {
      dataPointSelection: function(event, chartContext, config) {
        console.log(chartContext, config);
      }
    }
    },      
    series: [],
    }
  },
  methods: {
    async getInteractions(){
      let response = await axios({
          method: 'get',
          url: 'http://localhost:5000/interactions/api',
          headers: {
              'Content-Type': 'application/json',
              "Access-Control-Allow-Origin": "*"
          }
      })
      let sectorNames = []
      let sectorIDs = []
      response.data.forEach(sector => {
        sectorNames.push(sector['sector_name'])
        sectorIDs.push(sector['items'].length)
      });
      this.options.labels = sectorNames;
      this.series = sectorIDs;
      this.interactions = response.data
    },
    clickHandler(event, chartContext, config){
        this.show = true;
        this.interactions.forEach(interaction => {
          if(interaction['sector_name'] == this.options.labels[config.dataPointIndex]){
            this.tableBody = interaction['items']
          }
        })

    },
  },
  mounted(){
      this.getInteractions();
  }
}
</script>

<style scoped>
div.chart-wrapper {
  display: flex;
  align-items: center;
  justify-content: center 
}

</style>