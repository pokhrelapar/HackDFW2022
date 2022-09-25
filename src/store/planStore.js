import create from 'zustand';
import axios from 'axios';


const usePlanStore = create(set => ({
	plans: [],
	getPlans: async (selectedLocation) => {
		const response = await axios.get(`http://127.0.0.1:5000/plans/${selectedLocation}`);
		set({plans: (response.data)})
	},
	selectedPlan: null
}))

export default usePlanStore;