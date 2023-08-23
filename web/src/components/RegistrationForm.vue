<script setup>
import { ref } from 'vue';

const newUser = ref({
    username: null,
    email: null,
    password1: null,
    password2: null,
});


const registerUser = async () => {
    try {
        const response = await fetch("http://localhost:8000/dj-rest-auth/registration/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(newUser.value),
        });

        if (response.ok) {
            console.log(response)
        } else {
            // Do something with the error
        }
    } catch (error) {
        console.error("Registration error:", error);
    }
}

</script>

<template>
    <div>
        <h2>Register</h2>
        <form @submit.prevent="registerUser">
            <label for="username">Username:</label>
            <input type="text" id="username" v-model="newUser.username" required autocomplete="off">
            <br />
            <label for="email">Email:</label>
            <input type="email" id="email" v-model="newUser.email" required autocomplete="off">
            <br />
            <label for="password1">Password:</label>
            <input type="password" id="password1" v-model="newUser.password1" required autocomplete="off">
            <br />
            <label for="password2">Confirm Password:</label>
            <input type="password" id="password2" v-model="newUser.password2" required autocomplete="off">
            <br />
            <button type="submit">Register</button>
        </form>
    </div>
</template>