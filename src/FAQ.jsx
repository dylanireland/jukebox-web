export default function FAQ() {
	const faqs = {
		"How do I listen to Jukebox?":
			"To listen, simply visit the <a href='app' class='colorfulLink'>Jukebox dApp</a> and press play! Once you've done so, the queue will continue to play until you pause it or close the tab.",
		"How do I add a song to Jukebox?":
			"To add a song to the Jukebox queue, visit the <a href='app' class='colorfulLink'>Jukebox dApp</a> and select \"Add Song\". You may provide a direct link to an audio file or a download link for an audio file. You may also input a YouTube video link to be converted to audio.",
		"Are there fees to use Jukebox?":
			"There are no fees for listening to music; it is free and always will be. Adding songs to the queue does however include fees paid in Ether and is more expensive the longer the queue and the longer the song. See <a href='economics' class='colorfulLink'>Fee Pricing</a>",
		"What happens to fees paid by song publishers?":
			"Fees paid in Ether are stored in a smart contract and will be used to swap for JUK tokens when v2 is released. See <a href='future-work' class='colorfulLink'>Future Work</a>",
		"Can I choose when my song plays?":
			"At this time, songs are added to the queue sequentially and it is not possible to select a block interval to have your song play. This may change in the future.",
		"Can I sell my time slot back to Jukebox?":
			"Currently, once you purchase the right to have your song played, it will play during the designated interval and cannot be changed or refunded. In v2, time slots will be able to be sold as NFTs. See <a href='future-work' class='colorfulLink'>Future Work</a>"
	};

	let elements = [];

	for (const [q, a] of Object.entries(faqs)) {
		elements.push(
			<div className="row">
				<div className="col-6">
					<h3>{q}</h3>
				</div>
				<div className="col-6">
					<p dangerouslySetInnerHTML={{ __html: a }}></p>
				</div>
			</div>
		);
	}

	return <>{elements}</>;
}
