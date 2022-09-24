import create from 'zustand';

const useLocationStore = create(set => ({
	locations: [
		{ id: 'dallas', name: 'Florida', desc: 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using' },
		{ id: 'san fransisco', name: 'Texas', desc: 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to usingIt is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using'},
		{ id: 'patterson', name: 'California', desc: 'desc'},
		{ id: 'wichita', name: 'New York', desc: 'desc'},
	],
	selectedLocation: null
}))

export default useLocationStore;