import { createStore } from 'vuex';

export default createStore({
  state: {
    editMode: false
  },
  getters: {
  },
  mutations: {
    setEditMode(state, editMode) { state.editMode = editMode; }
  },
  actions: {
  },
  modules: {
  }
});
