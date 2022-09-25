import create from 'zustand';



const useLocationStore = create(set => ({
	locations: [
		{ id: 'dallas', name: 'Dallas, TX', desc: 'Dallas, a modern metropolis in north Texas, is a commercial and cultural hub of the region. Downtown’s Sixth Floor Museum at Dealey Plaza commemorates the site of President John F. Kennedy’s assassination in 1963. In the Arts District, the Dallas Museum of Art and the Crow Collection of Asian Art cover thousands of years of art. The sleek Nasher Sculpture Center showcases contemporary sculpture.' },
		{ id: 'san fransisco', name: 'San Fransisco, CA', desc: 'San Francisco, officially the City and County of San Francisco, is a commercial and cultural center in Northern California. The city proper is the 17th most populous in the United States, and the fourth most populous in California, with 815,201 residents as of 2021.'},
		{ id: 'patterson', name: 'Patterson, GA', desc: 'Patterson is defined less by boundaries on a map than by the sense of shared values our residents hold dear. They take pride in maintaining a wholesome lifestyle, rich in cultural history, along with a deep commitment to the preservation of our environment and a progressive approach to local business.'},
		{ id: 'wichita', name: 'Wichita, Kansas', desc: 'Wichita is a city in south-central Kansas. Exploration Place features hands-on science exhibits and Kansas in Miniature, a display of animated models depicting 1950s Kansas. Old Cowtown Museum recreates 19th-century life with old buildings and costumed guides. Themed gardens at Botanica Wichita include a wildflower meadow and a Chinese garden. The Museum of World Treasures has Egyptian mummies and a T. rex skeleton.'},
	],
	selectedLocation: null
}))

export default useLocationStore;