<template>
	<div id="keyboardInputAuditioner">{{ keyboardInputString }}</div>

	<h1 id="mainTitle" class="display-1">John's Homepage</h1>

	<div id="sectionContainer">
		<div v-for="(section, i) in filteredSections">
			<h1>{{ section.title }}</h1>

			<div class="flexDiv">
				<TileButton v-for="link in section.links"
							:tile-button-title="link.title"
							:title="link.title"
							:imageURL="link.imageURL"
							:destinationURL="link.destinationURL">
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

		data()
		{
		    return {
                keyboardInputString: ""
            }
		},

		computed: {
			filteredSections() {
			    const filteredSections = [];

			    for (const section of this.sections)
				{
				    const links = [];

				    if (section.disabled === true) { continue; }

				    for (const link of section.links)
					{
                        if (link.disabled === true) { continue; }

					    if (link.title.toLowerCase().includes(this.keyboardInputString))
						{
						    links.push(link);
						}
					}

				    if (links.length > 0)
					{
					    filteredSections.push({
							...section,
							links
                        })
					}
                }

			    return filteredSections;
			},

			sections() {
				let idCounter = 0;

				for (const section of sections) {
					for (const link of section.links) {
						link._id = idCounter++;
					}
				}
				return sections;
			},

			loneFilteredTileButton() {
                if (this.filteredSections.length === 1 && this.filteredSections[0].links.length === 1)
                {
                    return document.querySelector(`[tile-button-title='${this.filteredSections[0].links[0].title}']`);
                }
			}
		},

		methods: {
            handleKeyboardInput(event)
            {
                const key = event.key;

                if (key.length === 1)
                {
                    this.keyboardInputString += key.toLowerCase();
                }
                else
                {
                    switch (key)
                    {
                        case "Enter":
                            if (this.loneFilteredTileButton !== undefined)
							{
							    this.loneFilteredTileButton.click();
							}
                            break;

                        case "Backspace":
                            this.keyboardInputString = this.keyboardInputString.slice(0, -1);
                            break;

                        case "Escape":
                        case "Clear":
                            this.keyboardInputString = "";
                            break;
                    }
                }
            }
		},

		mounted() { document.addEventListener("keyup", this.handleKeyboardInput); },
		unmounted() { document.removeEventListener("keyup", this.handleKeyboardInput); }
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

	#mainTitle
	{
		padding: 40px 20px 0;

		text-align: center;

		position: sticky;
		top: 0;

		background-color: rgba(255, 255, 255, .90);
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