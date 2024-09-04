import logo from "./assets/photos/logo.svg";
import logoWithExtras from "./assets/photos/logoWithExtras.svg";
import etherscanLogo from "./assets/photos/etherscan.svg";
import coverchain from "./assets/photos/coverchain.png";
import "./assets/css/index.css";
import FAQ from "./FAQ";

export default function Home() {
	return (
		<>
			<div id="homeBanner">
				<header className="header">
					<div id="navlogo">
						<img src={logo} alt="Jukebox Logo" />
						<div id="jukeboxName">Jukebox</div>
					</div>
					<div id="navbuttons">
						<button>Launch App</button>
						<button>Whitepaper</button>
					</div>
				</header>
				<div className="homeContainer">
					<div>
						<div id="forwardFacingDiv">
							<h1>Jukebox</h1>
							<h2>
								The world's first decentralized radio station, powered by the
								Ethereum blockchain
							</h2>
						</div>
						<div id="logoWithExtrasContainer">
							<img src={logoWithExtras} alt="Jukebox Logo with Blockchain" />
							<button
								id="learnMore"
								onClick={function () {
									window.location.href = "#play";
								}}
							>
								Learn More
							</button>
						</div>
					</div>
				</div>
			</div>

			<div id="play">
				<div>
					<h1>Play any Song for the World to Hear</h1>
					<p>
						Jukebox is a public, decentralized streaming application with a
						single queue of songs that anyone may add to. Add a song on the{" "}
						<a href="app" className="colorfulLink">
							Jukebox dApp
						</a>{" "}
						and everyone listening during your time slot will hear it. Fees for
						adding songs are calculated in USD, paid in Ether, and grow in price
						with the length of queue to balance supply and demand{" "}
						<a href="economics" className="colorfulLink">
							Economics
						</a>
					</p>
				</div>
				<div>
					<img id="coverchain" src={coverchain} alt="Blockchain of Cover Art" />
				</div>
			</div>

			<div id="listen">
				<div>
					<h1>
						Listen for Free
						<br />
						Anytime,
						<br className="mobileBR" /> Anywhere
					</h1>
					<div>
						<p>
							Visit the{" "}
							<a href="app" className="colorfulLink">
								Jukebox dApp
							</a>{" "}
							to listen to an infinite queue of music, selected by countless
							individuals like you.
							<br />
							Easy, Seamless, and Free.
						</p>
						<div id="desktopQueue">
							<div>
								<h4>Live Queue</h4>
								<div className="blob red"></div>
							</div>
							<table>
								<thead>
									<tr>
										<th>Title</th>
										<th>Artist</th>
										<th>Publisher</th>
										<th>Starting Block</th>
										<th>Ending Block</th>
									</tr>
								</thead>
								{/* For song in queue */}
								<tbody>
									<tr>
										<td>{/* sng.title */}</td>
										<td>{/* sng.artist */}</td>
										<td>
											<a
												href="https://etherscan.io/address/PUBLISHERADDY"
												target="_blank"
											>
												{/* sng.publisher|makeShorterAddy */}
											</a>
										</td>
										<td>{/* sng.start */}</td>
										<td>{/* sng.end */}</td>
									</tr>
								</tbody>
								{/* End for loop */}
							</table>
							<div>
								<a href="queue" className="colorfulLink">
									View Full Queue
								</a>
							</div>
						</div>
					</div>
				</div>
			</div>

			<div id="faq">
				<div>
					<h1>FAQ</h1>
				</div>
				<div className="container">
					<FAQ />
				</div>
			</div>

			<div id="roadMap">
				<div>
					<h1>Roadmap</h1>
				</div>
				<div className="timeline">
					<div className="containertime left">
						<div className="content">
							<h2>Jukebox alpha Sepolia Launch</h2>
							<p>
								Jukebox is officially live on the Sepolia Testnet! At this time,
								many aspects of the protocol are still in development.
							</p>
						</div>
					</div>
					<div className="containertime right">
						<div className="content">
							<h2>Jukebox v1 Mainnet Launch</h2>
							<p>Jukebox will be launched on the Ethereum Mainnet soon!</p>
						</div>
					</div>
					<div className="containertime left">
						<div className="content">
							<h2>Jukebox v2</h2>
							<p>
								Jukebox v2 will feature significant upgrades including the JUK
								token and NFT based time slots that can be bought and sold. See{" "}
								<a href="future-work" className="colorfulLink">
									Future Work
								</a>
							</p>
						</div>
					</div>
				</div>
			</div>

			<footer id="footer">
				<h3>&copy; 2021 Jukebox</h3>
				<div id="socialFooter">
					<a
						target="_blank"
						href="https://github.com/dylanireland/jukebox-core"
					>
						<svg
							xmlns="http://www.w3.org/2000/svg"
							width="16"
							height="16"
							fill="currentColor"
							className="bi bi-github"
							viewBox="0 0 16 16"
						>
							<path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z" />
						</svg>
					</a>
					<a
						target="_blank"
						href="https://rinkeby.etherscan.io/address/0xeA3E60804ee1e8D5eC46c889B5DCEfD3eE9EfB11"
					>
						<img src={etherscanLogo} />
					</a>
				</div>
			</footer>
		</>
	);
}
