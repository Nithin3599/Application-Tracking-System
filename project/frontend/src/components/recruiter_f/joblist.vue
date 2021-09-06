<template>
<div>
 <div class="createjob">
     <form @submit.prevent="createpost" class="wrapper">
      <h3>CREATE JOB</h3>
      <div class="field input">
        <label for="title">job title </label>
        <input type="text" id="title" v-model="formData.title" required/>
      </div>
      <div class="field input">
        <label for="skill">job skill </label>
        <input type="text" id="skill" v-model="formData.skill" required/>
      </div>
      <div class="field input">
        <label for="description">job description </label>
        <input type="text" id="description" v-model="formData.description" required/>
      </div>
      <div class="cbutton">
        <button>create</button>
      </div>
    </form>
 </div>
  <div>
    <div v-for="post in posts" :key="post.job_id" class="showjob">
      <div>
        <h3>JOB ID:{{ post.job_id }}</h3>
        <h3>JOB TITLE: {{ post.title }}</h3>
        <h4>JOB SKILL: {{ post.skill }}</h4>
        <h4>JOB DESCRIPTION:</h4>
        <p>{{ post.description }}</p>
        <div class="ebutton">
          <button @click="updatepost(post)">Edit</button>
        </div>
        <div class="dbutton">
          <button @click="deletepost(post.job_id)">Delete</button>
        </div>
        <div v-if="edit_job_id == post.job_id" class="edit input">
          <form @submit.prevent="editpost">
            <div class="Showjob-heading">
              <label for="title">job title</label>
              <input type="text" id="title" v-model="formData.title" />
            </div>
            <div class="Showjob-skills">
              <label for="skill">job skill</label>
              <input type="text" id="skill" v-model="formData.skill" />
            </div>
            <div class="Showjob-description">
              <label for="description">job description</label>
              <input
                type="text"
                id="description"
                v-model="formData.description"
              />
            </div>
            <div class="ubutton">
              <button >update post</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from "axios";

export default {
  name: "joblist",
  created() {
    this.getPosts();
  },
  data() {
    return {
      posts: [],
      edit_job_id: 0,
      formData: {
        job_id: "",
        title: "",
        skill: "",
        description: "",
      },
      userdetail: {
        user_id: "",
      },
      update_Data: {
        title: "",
        skill: "",
        description: "",
      },
    };
  },

  methods: {
     createpost() {
      axios
        .post("http://127.0.0.1:8000/jobs/", this.formData)
         .then((response) => this.getPosts())
        .catch((error) => console.log(error));
    },
    getPosts() {
      axios
        .get("http://127.0.0.1:8000/jobs/?skip=0&limit=100")
        .then((response) => {
          this.posts = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    updatepost(post) {
      this.formData = post;
      this.edit_job_id = post.job_id;
    },
    editpost() {
      axios
        .put(`http://127.0.0.1:8000/jobs/${this.formData.job_id}`,this.formData)
        .then((response) =>{
          this.getPosts()
          this.edit_job_id = 0;
        }  )
        .catch((error) => console.log(error));
    },

    deletepost(job_id) {
      axios
        .delete(`http://127.0.0.1:8000/jobs/${job_id}/`)
        .then((response) => this.getPosts())
        .catch((error) => console.log(error));
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
.ubutton button {
  margin: 13px;
  border: none;
  font-size: 17px;
  font-weight: 400;
  background: rgb(35, 151, 113);
  color: black;
  border-radius: 5px;
  height: 45px;
  width: 85px;
}
.input input {
  width: 10px;
  font-size: 16px;
  padding: 0 10px;
  border-radius: 5px;
  margin-top: 10px;
  margin-bottom: 10px;
}
.createjob {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 20vh;
}
.wrapper {
  background: #fff;
  padding: 25px 30px;
  width: 450px;
  border-radius: 16px;
  box-shadow: 0 0 50px 0 rgba(0, 0, 0, 0.1),
    0 32px 64px -48px rgba(0, 0, 0, 0.5);
}
.field {
  display: flex;
  flex-direction: column;
  margin-top: 10px;
  margin-bottom: 10px;
  font-style: times;
}
.input input {
  height: 40px;
  width: 100%;
  font-size: 16px;
  padding: 0 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.cbutton button {
  margin: 13px;
  border: none;
  font-size: 17px;
  font-weight: 400;
  background: grey;
  color: #fff;
  border-radius: 5px;
  height: 45px;
  width: 75px;
}
</style>