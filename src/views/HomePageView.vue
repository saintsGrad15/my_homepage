<template>
	<div id="keyboardInputAuditioner">{{ keyboardInputString }}</div>

	<div id="sectionContainer">
		<div v-for="(section, i) in filteredSections">
			<h1>{{ section.title }}</h1>

			<div class="flexDiv">
				<TileButton v-for="link in section.links"
							:tile-button-title="link.title"
							:title="link.title"
							:imageURL="link.imageURL"
							:destinationURL="link.destinationURL"
							:_id="link._id"
							:tabSelectedId="tabSelectedId">
				</TileButton>
			</div>

			<hr v-if="i < filteredSections.length - 1">
		</div>
	</div>
</template>

<script>
    import TileButton from "@/components/TileButton.vue";
    import sections from '@/assets/sections.json';
	
    export default {
        name: "HomePageView",
		components: { TileButton },

		data() {
		    return {
		        keyboardInputString: "",
				tabSelectedId: null
            }
		},

		computed: {
			isSearching() {
				return this.keyboardInputString.length > 0;
			},

			filteredSections() {
			    const filteredSections = [];

			    for (const section of this.sections) {
				    const links = [];

				    if (section.disabled === true) { continue; }

				    for (const link of section.links) {
                        if (link.disabled === true) { continue; }

					    if (link.title.toLowerCase().includes(this.keyboardInputString)) {
						    links.push(link);
						}
					}

				    if (links.length > 0) {
					    filteredSections.push({
							...section,
							links
                        })
					}
                }

			    return filteredSections;
			},

			filteredLinks() {
				const filteredLinks = [];

				for (const filteredSection of this.filteredSections) {
					for (const link of filteredSection.links) {
						filteredLinks.push(link);
					}
				}

				return filteredLinks;
			},

			filteredLinksIdMap() {
				const filteredLinksIdMap = {};

				for (const filteredLink of this.filteredLinks) {
					filteredLinksIdMap[filteredLink._id] = filteredLink;
				}

				return filteredLinksIdMap;
			},

			sections() {
				let idCounter = 0;

				for (const section of sections) {
					for (const link of section.links) {
						link._id = idCounter++;
					}
				}
				return sections;
			}
		},

		watch: {
			isSearching(value) {
				if (value) {
					if (this.tabSelectedId === null) {
						this.tabSelectedId = this.filteredLinks[0]._id;
					}
				}
			},

			keyboardInputString(value) {
				const filteredIds = Object.keys(this.filteredLinksIdMap);

				if (this.tabSelectedId !== null && !filteredIds.includes(this.tabSelectedId.toString())) {
					this.tabSelectedId = Number.parseInt(filteredIds.sort()[0]);
				}
			},

			tabSelectedId(value) {
				if (value !== null) {
					document.querySelector(`a.btn[_id='${value}']`).scrollIntoView( {block: "center"} );
				}
			}
		},

		methods: {
			handleKeyDown(event) {
				if (event.key === "Tab") {
					event.preventDefault();
				}
			},
            handleKeyUp(event) {
				const key = event.key;

				switch (key) {
					case "Enter":
						if (this.tabSelectedId !== null) {
							window.open(this.filteredLinksIdMap[this.tabSelectedId].destinationURL,
							event.altKey ? "_blank" : "_self");
						}
						break;

					case "Backspace":
						this.keyboardInputString = this.keyboardInputString.slice(0, -1);
						break;

					case "Escape":
					case "Clear":
						if (this.keyboardInputString.length < 1) {
							this.tabSelectedId = null;
						}
						else {
							this.keyboardInputString = "";
						}
						break;

					case "Tab":
						if (event.shiftKey) {  // Tab backward
							if (this.tabSelectedId === null) {
								if (this.filteredLinks.length > 0) {
									this.tabSelectedId = this.filteredLinks[this.filteredLinks.length - 1]._id;
								}
							}
							else {
								for (const [index, link] of this.filteredLinks.entries()) {
									if (this.tabSelectedId === link._id) {
										// The first element
										if (index === 0) {
											this.tabSelectedId = this.filteredLinks[this.filteredLinks.length - 1]._id;
										}
										else {
											this.tabSelectedId = this.filteredLinks[index - 1]._id;
										}

										break;
									}
								}
							}
						}
						else {  // Tab forward
							if (this.tabSelectedId === null) {
								if (this.filteredLinks.length > 0) {
									this.tabSelectedId = this.filteredLinks[0]._id;
								}
							}
							else {
								for (const [index, link] of this.filteredLinks.entries()) {
									if (this.tabSelectedId === link._id) {
										// The last element
										if (index === this.filteredLinks.length - 1) {
											this.tabSelectedId = this.filteredLinks[0]._id;
										}
										else {
											this.tabSelectedId = this.filteredLinks[index + 1]._id;
										}

										break;
									}
								}
							}
						}

						break;
					default:
						if (key.length === 1) {
							this.keyboardInputString += key.toLowerCase();
						}
						break;
				}
            }
		},

		mounted() {
			document.addEventListener("keydown", this.handleKeyDown);
			document.addEventListener("keyup", this.handleKeyUp);
		 },
		unmounted() {
			document.removeEventListener("keydown", this.handleKeyDown);
			document.removeEventListener("keyup", this.handleKeyUp);
		}
    }
</script>

<style scoped>
	#keyboardInputAuditioner
	{
		position: absolute;
		top: 5px;
		right: 5px;

		padding: 0 5px;

		background-color: lightgray;

		z-index: 1;
	}

	#sectionContainer
	{
		display: grid;

		grid-template-columns: 1fr;

		grid-column-gap: 10px;
	}

	@media (min-width: 775px)
	{
		#sectionContainer
		{
			grid-template-columns: repeat(2, 1fr);
		}
	}

	.flexDiv
	{
		display: flex;
		flex-wrap: wrap;

		gap: 30px;
	}
</style>