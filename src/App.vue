<template>
  <div id="mainTitleArea">
    <div v-if="editMode === true" class="toggleEditButtonContainer">
      <button type="button" class="toggleEditButton btn btn-danger" @click="cancelChanges">
        <i class="bi bi-x-square fontSize1_5Rem"></i>
        <div class="editButtonText">Cancel</div>
      </button>
      <button type="button" class="toggleEditButton btn btn-success" @click="saveChanges">
        <i class="bi bi-save fontSize1_5Rem"></i>
        <div class="editButtonText">Save</div>
      </button>
    </div>

    <div v-else class="toggleEditButtonContainer">
      <button type="button" class="toggleEditButton btn btn-info" @click="enterEditMode">
        <i class="bi bi-pencil fontSize1_5Rem"></i>
        <div class="editButtonText">Edit</div>
      </button>
    </div>

    <h1 id="mainTitle" class="display-1">
      John's Homepage
    </h1>

    <hr id="mainTitleHR"/>
  </div>

  <div id="appContent">
    <router-view/>
  </div>
</template>

<script>
    import store from '@/store';
    import { mapMutations } from 'vuex';

    export default {
      name: 'App',

      computed: {
        editMode() { return store.state.editMode; }
      },

      methods: {
        ...mapMutations([
          'setEditMode',
        ]),
        enterEditMode() {
          this.setEditMode(true);
        },

        cancelChanges() {
          this.setEditMode(false);
        },

        saveChanges() {}
      }
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

#mainTitleArea
{
  display: grid;

  grid-template-columns: 1fr max-content;

  align-content: center;
}

#mainTitle
{
  grid-row: 1;
  grid-column: 1 / -1;

  padding: 40px 20px 0;

  text-align: center;

  background-color: rgba(255, 255, 255, .90);
}

.toggleEditButtonContainer
{
  grid-row: 1;
  grid-column: 2;

  z-index: 1;
}

.toggleEditButton
{
  border-radius: 0;

  height: 100%;
  width: 70px;
}

.toggleEditButtonText
{
  margin-top: 10px;
}

#mainTitleHR
{
  grid-row: 2;
  grid-column: 1 / -1;

  margin: 0;
}

#appContent
{
  height: 100%;
  overflow-y: scroll;

  padding-bottom: 40px;
  padding: 16px 40px 40px 40px;
}

nav { padding: 30px; }

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active { color: #42b983; }

.fontSize1_5Rem  { font-size: 1.5rem; }
</style>
