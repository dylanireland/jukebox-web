class Contract:
    def getAbi():
        return '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"start","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"end","type":"uint256"},{"indexed":false,"internalType":"string","name":"url","type":"string"},{"indexed":false,"internalType":"string","name":"coverUrl","type":"string"},{"indexed":false,"internalType":"string","name":"title","type":"string"},{"indexed":false,"internalType":"string","name":"artist","type":"string"},{"indexed":false,"internalType":"address","name":"publisher","type":"address"}],"name":"SongAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"end","type":"uint256"},{"indexed":true,"internalType":"string","name":"url","type":"string"},{"indexed":true,"internalType":"string","name":"title","type":"string"}],"name":"queueUp","type":"event"},{"inputs":[{"internalType":"string","name":"url","type":"string"},{"internalType":"string","name":"coverUrl","type":"string"},{"internalType":"string","name":"title","type":"string"},{"internalType":"string","name":"artist","type":"string"},{"internalType":"uint256","name":"duration","type":"uint256"}],"name":"addSong","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getCurrentSong","outputs":[{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getNextStartTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getQueueDepth","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getQueueLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getSongAtIndex","outputs":[{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"queue","outputs":[{"internalType":"uint256","name":"start","type":"uint256"},{"internalType":"uint256","name":"end","type":"uint256"},{"internalType":"string","name":"url","type":"string"},{"internalType":"string","name":"coverUrl","type":"string"},{"internalType":"string","name":"title","type":"string"},{"internalType":"string","name":"artist","type":"string"},{"internalType":"address","name":"publisher","type":"address"}],"stateMutability":"view","type":"function"}]'

    def getAddy():
        return "0x956c9f39101bC919595856964929dbAeE0DD4096"

    def getinfUrl():
        return "https://rinkeby.infura.io/v3/d737ea73e7034c099c511477264a3ae5"