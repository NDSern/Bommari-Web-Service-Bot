import {ArrowUpOutline} from "react-ionicons";
import "../css/ToTopButton.sass";

export default function ToTopButton() {
	return (
		<div className={"to-top-button rounded-circle text-bg-light p-2 shadow"} onClick={() => window.scroll(0, 0)}>
			<ArrowUpOutline
				color={'#00000'}
				title={"Scroll To Top"}
				height="30px"
				width="30px"
			/>
		</div>
	);
};