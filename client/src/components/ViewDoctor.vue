<template>
    <center>
        <div id="wrapper">
            <div id="about">
                <img id="image" width="35%" :src="doctor.photo"/>
                <h1>{{ doctor.name }}</h1>
                <h2 id="methods_header"> Методы </h2>
                <div id="methods" v-for="method in doctor.methods" :key="method">
                    <p>{{ method }}</p>
                </div>
            </div>
        </div>
    </center>
</template>

<script>
import { findDoctor } from "../helpers/doctors"

export default {
    name: "ViewDoctor",
    computed: {
        doctor () {
            return findDoctor(this.$store.getters.DOCTORS, this.$route.params.id)
        }
    }
}
</script>

<style>
#about {
    text-align: left;
}

#about img {
    float: left;
    margin-right: 20px;
}

#image {
    margin: auto;
}

#methods {
    margin-top: -30px;
}

#methods_header {
    margin-top: -10px;
    margin-bottom: 45px;
}

#methods p {
    float: left;
    padding: 5px;
    background: #E8E8E8;
    margin-right: 10px;
    margin-top: -10px;
    padding-left: 10px;
    padding-right: 10px;
}
</style>