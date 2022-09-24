import create from 'zustand';

const useScenarioStore = create(set => ({
	scenarios: [
		{id: 'fire', header: 'A fire has burned down your home!', desc: 'desc'},
		{id: 'hurricane', header: 'A hurricane has ripped the roof off your home!', desc: 'desc'},
		{id: 'tornado', header: 'A tornado has blown your home away!', desc: 'desc'},
		{id: 'flood', header: 'A flash flood has destroyed your basement!', desc: 'desc'},
	]
}))

export default useScenarioStore;