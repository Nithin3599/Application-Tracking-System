<template>
  <div id="app">
    <h1>Job Details</h1>
      
    <joblist> </joblist>
    
  </div>
</template>

<script>
//import joblist from "./joblist.vue"
//import createpost from './createpost.vue';
import joblist from "./recruiter_f/joblist.vue"

export default {
  name: "App",
  components: {
    joblist,
    
  },
};
</script>

<style lang="scss">
* {
  box-sizing: border-box;
}

html, body {
  padding: 0;
  margin: 0;
  background-color: #efefef;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  padding: 24px;
  max-width: 1000px;
  margin: auto;
}

.jobslist {
  &-button {
    padding: 8px;
    margin-right: 16px;
    min-width: 96px;
    border: 0;
    box-shadow: 0 2px 4px #ccc;
    border-radius: 2px;
    cursor: pointer;
    transition: all 0.225s;
    background-color: #0ff;

    &:hover {
      box-shadow: 0 4px 8px #ccc;
      background-color: darken(#0df, 8%);
    }

    &--danger {
      background-color: #f55;

      &:hover {
        background-color: darken(#f55, 8%);
      }
    }
  }

  &-control {
    margin-bottom: 8px;

    &--l {
      input {
        width: 100%;
      }
      
      textarea {
        width: 100%;
        height: 200px;
      }
    }
  }

  &-input {
    padding: 8px;
    border: 1px solid #ccc;
    margin-right: 8px;

    &::placeholder {
      color: #aaa;
    }
  }

  &-label {
    display: block;
  }
}
</style>
