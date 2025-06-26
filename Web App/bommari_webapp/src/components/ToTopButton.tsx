import { IoArrowUpOutline } from "react-icons/io5";
import "../css/ToTopButton.sass";

export default function ToTopButton() {
	return (
		<div className={"to-top-button rounded-circle text-bg-light p-2 shadow"} onClick={() => window.scroll(0, 0)}>
			<IoArrowUpOutline
				color={'#00000'}
				title={"Scroll To Top"}
				size={30}
			/>
		</div>
	);
};