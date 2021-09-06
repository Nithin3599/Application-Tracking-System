<template>
  <div class="createjob">
    <form @submit.prevent="createcandidate" class="wrapper">
      <h3>CREATE CANDIDATE</h3>
      <div class="field input">
        <label for="candidate_name">Candidate Name</label>
        <input
          type="text"
          id="candidate_name"
          v-model="formData.candidate_name"
          required
        />
      </div>
      <div class="field input">
        <label for="email">Email ID</label>
        <input type="text" id="email" v-model="formData.email" required />
      </div>
      <div class="field input">
        <label for="password">password</label>
        <input type="text" id="password" v-model="formData.password" required />
      </div>
      <div class="cbutton">
        <button>create</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "createcandidate",
  data() {
    return {
      formData: {
        candidate_name: "",
        email: "",
        password: "",
      },
    };
  },
  methods: {
    createcandidate() {
      axios
        .post("http://127.0.0.1:8000/users/", this.formData)
        .then((response) => console.log(response))
        .catch((error) => console.log(error));
    },
  },
};
</script>

<style>
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