<template>
  <div>
    <div v-for="post in posts" :key="post.job_id" class="showjob">
      <div>
        <h3>JOB ID:{{ post.job_id }}</h3>
        <h3>JOB TITLE: {{ post.title }}</h3>
        <h4>JOB SKILL: {{ post.skill }}</h4>
        <h4>JOB DESCRIPTION:</h4>
        <p>{{ post.description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
//import editjob from "./components/editjob.vue";

export default {
  name: "jobslist",
  created() {
    this.getPosts();
  },
  data() {
    return {
      posts: [],
      num: 0,
      formData: {
        job_id: "",
        title: "",
        skill: "",
        description: "",
      },
    };
  },

  methods: {
    getPosts() {
      axios
        .get("http://127.0.0.1:8000/jobs/?skip=0&limit=100")
        .then((response) => {
          console.log(response.data);
          this.posts = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style  lang="scss">
.showjob {
  background-color: #fff;
  padding: 24px;
  margin-top: 24px;
  margin-bottom: 24px;
  box-shadow: 0 4px 8px #888;
}
.showjob-skills {
  list-style-type: none;
  padding: 0;
  background: black;
}

.skill {
  display: inline-block;
  margin-right: 8px;
  padding: 8px;
  background-color: #eee;
}
.ebutton button {
  margin: 13px;
  border: none;
  font-size: 17px;
  font-weight: 400;
  background: skyblue;
  color: black;
  border-radius: 5px;
  height: 45px;
  width: 75px;
}
.dbutton button {
  margin: 13px;
  border: none;
  font-size: 17px;
  font-weight: 400;
  background: rgb(230, 65, 65);
  color: black;
  border-radius: 5px;
  height: 45px;
  width: 75px;
}
</style>