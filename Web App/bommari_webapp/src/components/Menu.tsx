import {Container, Image,} from "react-bootstrap";

export default function Menu() {
	return (
		<Container className="bg-warning pt-2 pb-3 shadow" fluid>
			<div className="d-flex justify-content-between">
				<Image src="/public/cropped-cropped-tekiila_outline-1.png" height={"60rem"}/>
			</div>
		</Container>
	);
}
