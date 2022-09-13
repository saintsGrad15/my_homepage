<template>
	<a class="btn btn-outline-dark tileButton"
	   :href="editMode === true ? null : destinationURL"
	   :class="{'tabSelected': _id === tabSelectedId, 'editMode': editMode}"
	   :_id=_id>
		<div class="tileButtonBase">
			<img class="buttonImage" v-if="imageURL !== undefined && imageURL.length > 0" :src="imageURL">
			<div class="buttonText">{{ title }}</div>
		</div>
		<div v-if="editMode === true" class="tileButtonEditOverlay">
			<button type="button" class="btn btn-danger">
				<i class="bi bi-trash3"></i>
				<div>Delete</div>
			</button>
			<button type="button" class="btn btn-success">
				<i class="bi bi-pencil"></i>
				<div>Edit</div>
			</button>
			<button type="button" class="btn btn-info">
				<i class="bi bi-caret-left"></i>
				<div>Move</div>
			</button>
			<button type="button" class="btn btn-info">
				<i class="bi bi-caret-right"></i>
				<div>Move</div>
			</button>
		</div>
	</a>
</template>

<script>
	import store from '@/store';

    export default {
        name: "TileButton",

		props: ["title", "imageURL", "destinationURL", "_id", "tabSelectedId"],

		computed: {
			editMode() { return store.state.editMode; }
		}
    }
</script>

<style scoped>
	.tileButton
	{
		display: grid;
	}

	.tileButton.editMode:hover
	{
		background-color: white;
	}

	.tileButton > .tileButtonBase
	{
		position: static;

		grid-column: 1;
		grid-row: 1;

		width: 150px;
		height: 150px;

		display: flex;
		flex-direction: column;

		justify-content: space-evenly;
		align-items: center;
	}

	.tileButton > .tileButtonEditOverlay
	{
		grid-column: 1;
		grid-row: 1;

		display: grid;

		grid-template-columns: repeat(2, 1fr);
		grid-template-rows: repeat(2, 1fr);
	}

	.tileButton:not(:hover) > .tileButtonEditOverlay
	{
		opacity: 10%;
	}

	.tileButton > .tileButtonEditOverlay > button
	{
		border-radius: 0;

		border: solid 0.5px black;
	}

	.tileButton > .tileButtonEditOverlay > button:nth-child(1) { border-top-left-radius: 0.375rem; }
	.tileButton > .tileButtonEditOverlay > button:nth-child(2) { border-top-right-radius: 0.375rem; }
	.tileButton > .tileButtonEditOverlay > button:nth-child(3) { border-bottom-left-radius: 0.375rem; }
	.tileButton > .tileButtonEditOverlay > button:nth-child(4) { border-bottom-right-radius: 0.375rem; }

	.tileButton > .tileButtonEditOverlay > button:focus
	{
		box-shadow: unset;
	}

	.tileButton.editMode:hover > .tileButtonBase
	{
		visibility: hidden;
	}

	.tileButton.tabSelected {
		box-shadow: 0px 0px 5px 3px;
	}

	.tileButton > .tileButtonBase > .buttonImage {
		max-width: 50px;
		max-height: 50px;
	}
</style>