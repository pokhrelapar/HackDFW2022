import create from 'zustand';

const usePlanStore = create(set => ({
	plans: [
		{id: 'P1', header: 'Premium + Hurricane Coverage', desc: 'Annual Policy Premium: $4,802\nGeneral Policy Deductible: $3,440\nWindstorm Coverage Deductible: $17,200'},
		{id: 'P2', header: 'Basic + Tornado Coverage', desc: 'Annual Policy Premium: $1,205\nGeneral Policy Deductible: $5,000\nTornado Coverage Deductible: $13,100'},
		{id: 'P3', header: 'Premium', desc: 'Annual Policy Premium: $4,802\nGeneral Policy Deductible: $3,440\n'},
		{id: 'P4', header: 'Basic', desc: 'Annual Policy Premium: $1,205\nGeneral Policy Deductible: $5,000\n'},
	]
}))

export default usePlanStore;