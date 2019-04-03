<template>
    <div id="app">
        <ul>
            <h1> HELLO </h1>
            <li v-for="i in items" :key="i.id">
                <p> {{ i.id }} </p>
            </li>
        </ul>
    </div>

</template>
<script src="../scripts/data.js"/>
