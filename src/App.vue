<template>
	<h1 id="mainTitle" class="display-1">
    John's Homepage
    <hr/>
  </h1>

  <div id="appContent">
    <router-view/>
  </div>
</template>

<script>
    export default {
        name: 'App'
    }
</script>

<style>
html, body, #app { height: 100%; }

html { overflow-y: hidden; }

#app
{
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;

  display: grid;
  grid-template-rows: max-content 1fr;
}

#mainTitle
{
  padding: 40px 20px 0;

  text-align: center;

  background-color: rgba(255, 255, 255, .90);
}

#appContent
{
  height: 100%;
  overflow-y: scroll;

  padding-bottom: 40px;
  padding: 0 40px 40px 40px;
}

nav { padding: 30px; }

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active { color: #42b983; }
</style>
