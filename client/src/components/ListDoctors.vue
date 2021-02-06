<template>
    <center>
        <div id="wrapper">
            <div id="header">
                <h1> Психотерапевты </h1>
            </div>
            <div id="list" v-for="doctor in doctors" v-bind:key="doctor.id">
                <router-link id="route-link" :to="doctor.path">
                    <div id="list-item">
                        <p>{{ doctor.id }} <b>{{ doctor.name }}</b> </p>
                    </div>
                </router-link>
            </div>
        </div>
    </center>
</template>

<script>
import { getDoctorsList } from "../helpers/doctors"

export default {
    name: "ListDoctors",
    computed: {
        doctors () {
            return getDoctorsList(this.$store.getters.DOCTORS)
        }
    }
}
</script>

<style>
#wrapper {
    width: 55%;
    display: flex;
    flex-direction: column;
}

#header {
    text-align: left;
}

#list {
    display: flex;
    flex-direction: column
}

#list-item {
    text-align: left;
    cursor: pointer;
    border-radius: 11px 11px 11px 11px;
    -moz-border-radius: 11px 11px 11px 11px;
    -webkit-border-radius: 11px 11px 11px 11px;
    border: 0px solid #000000;
    padding-top: 5px;
    padding-bottom: 5px;
    padding-left: 10px;
    padding-right: 10px;
    transition: 0.5s;
}

#route-link {
    text-decoration: none;
}

#list-item p {
    color: #c9c9c9;
}

#list-item b {
    color: #000000;
}

#list-item:hover {
    background-color: #f2f2f2;
}
</style>