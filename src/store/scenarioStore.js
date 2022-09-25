import create from 'zustand';
// import axios from 'axios';
const useScenarioStore = create(set => ({
	scenarios: [
		{id: 'earthquake', header: 'There was a devastating 8.4 magnitude earthquake nearby!', desc: 'Your house sustained $92,500 in structural damage and you will need to file a claim!', result: 'Luckily, you included earthquake coverage with your State Farm homeowner\'s insurance and they\'re here to help! You will only pay up to your deductible amount of $42,900, and State Farm will cover the remaining amount.'},
		{id: 'hurricane', header: 'A hurricane has ripped the roof off your home!', desc: 'desc', result: ''},
		{id: 'tornado', header: 'A tornado has blown your home away!', desc: 'desc', result: ''},
		{id: 'flood', header: 'A flash flood has destroyed your basement!', desc: 'desc', result: ''},
	]
}))

export default useScenarioStore;