export default [
    {
        header: "Home",
        slug: 'home',
        url: '',
        icon: 'bx-home'
    },
    {
        header: "USSD",
        icon: 'bx-dialpad',
        items: [
            {
                url: '/',
                name: 'Flows',
                slug: 'flows',
                icon: 'bx-network-chart'
            },
            {
                url: 'about',
                slug: 'aggregator_apis',
                name: 'Aggregator APIs',
                icon: 'bx-plug'
            }
        ]
    },
    {
        header: "SMS",
        url: '',
        slug: 'sms',
        icon: 'bx-chat'
    },
    {
        header: "SMS GATEWAYS",
        icon: 'bxs-cog',
        items: [
            {
                url: '/',
                name: 'Kannel',
                slug: 'kannel',
                icon: 'bxs-inbox'
            },
            {
                url: 'about',
                name: 'Mbuni',
                slug: 'mbuni',
                icon: 'bx-station'
            }
        ]
    },
    {
        header: "Donate",
        url: '',
        slug: 'donate',
        icon: 'bxs-donate-heart'
    },
    {
        header: "Help",
        url: '',
        slug: 'help',
        icon: 'bx-help-circle'
    },

]