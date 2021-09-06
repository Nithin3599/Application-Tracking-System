<template>
  <div >
    <div class="job">
    <router-link to="/jobpath">recruiter</router-link><br/><br/>
    <router-link to="/candidatepath">candidate</router-link>
    </div>
    
    <router-view></router-view>
  </div>
</template>

<script>
import appc from "./components/appc.vue";
import appr from "./components/appr.vue";
export default {
  components: { appc, appr},
  name: "App",
  data() {
    return {
     
    };
  },
};
</script>

<style lang="scss">


</style>
