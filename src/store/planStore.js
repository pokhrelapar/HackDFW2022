import create from 'zustand';

const usePlanStore = create(set => ({
	plans: [
		{id: 'P1', header: 'Premium + Hurricane Coverage', desc: 'desc'},
		{id: 'P2', header: 'Basic + Tornado Coverage', desc: 'desc'},
		{id: 'P3', header: 'Premium', desc: 'desc'},
		{id: 'P4', header: 'Basic', desc: 'desc'},
	]
}))

export default usePlanStore;