<template>
  
  <div id="app">

    <div class="columns">

      <div class="column is-2">

        <aside class="menu" style="padding:20px 20px 0;position:fixed; top:0; left:0;">
        
          <p class="menu-label">
            Options
          </p>

          <ul class="menu-list">
            <li><a>Overview</a></li>
            <li><a>Reports</a></li>
            <li><a>Statistics</a></li>
          </ul>

        </aside>

      </div>

      <div class="column is-10">

        <h1 class="pb-6 is-size-3" style="padding:25px 0;">My Projects</h1>

        <div class="columns" style="display:flex;flex-wrap:wrap;justify-content: flex-start;">

          <div class="column is-3"
               v-for="project in projects"
               v-bind:key="project.id">
            
            <div class="card progress-container mr-6">
              
              <div class="card-content">
                
                <div class="content">           
    
                  <p class="project-title">{{ project.name }} </p>
    
                  <div class="statistics-container">
                    
                    <div class="progress-details">
                      <span class="progress-type">Current tasks</span>
                      <span class="progress-value">12%</span>
                    </div>
    
                    <b-progress :value="12" type="is-success" size="is-small"/>
    
                  </div>
    
                  <div class="statistics-container">
                    
                    <div class="progress-details">
                      <span class="progress-type">Remain tasks</span>
                      <span class="progress-value">5/15</span>
                    </div>
    
                    <b-progress :value="20" type="is-info" size="is-small"/>
    
                  </div>
    
                  <div class="statistics-container">
                    
                    <div class="progress-details">
                      <span class="progress-type">Current deadline</span>
                      <span class="progress-value">5 days</span>
                    </div>
    
                    <b-progress :value="20" type="is-danger" size="is-small"/>
    
                  </div>
                  
                </div>    
                
                <div class="card-bottom">
    
                    <b-button 
                    size="is-small" 
                    type="is-info" 
                    icon-right="arrow-right" 
                    class="access-button">Acess</b-button>
    
                </div>
    
              </div>
              
            </div>
    
          </div>      
    
        </div>

      </div>

    </div>

  </div>
</template>

<style>

#app {
  font-family: 'Roboto', sans-serif;
  margin:0;
  padding:0;
}

.progress-container{
  width:300px !important;
}

.statistics-container{
  display:flex;
  flex-direction: column;
  margin-bottom:15px;
}

.project-title{
  color: #636e72;
  text-align:center;
  font-size:20px;
  font-weight:bold;
  letter-spacing:1px;
}

.progress-details{
    display:flex;
    flex-direction:row;
    justify-content: space-between;
    align-items:center;
}

.progress-type{
  color: #636e72;
  letter-spacing:0.5px;
  font-size:15px;
  margin-bottom:3px;
  display:flex;
  justify-content: space-between;
}

.progress-value{
  font-weight:bold;
  font-size:15px;
  color:#636e72;
}

.card-bottom{
  width:100%;
  margin:0 auto;
  text-align:right;
}


</style>

<script>

import projectService from "@/services/projectService.js";

export default {

    data() {
      return {
        projects: null,
      }
    },

    mounted() {
      projectService.all().then(response => (this.projects = response))
    }
     
}

</script>
