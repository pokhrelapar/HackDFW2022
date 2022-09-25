import create from 'zustand';
import axios from 'axios';


const useLocationStore = create(set => ({
	locations: [],
	getLocations: async () => {
		const response = await axios.get('http://127.0.0.1:5000/location');
		set({ locations: response.data});
	},
	selectedLocation: null,
}))

export default useLocationStore;