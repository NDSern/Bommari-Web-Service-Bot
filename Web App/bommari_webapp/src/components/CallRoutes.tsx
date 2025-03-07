
import Card from "react-bootstrap/Card";
import { Route } from "../types/route";
import { Container } from "react-bootstrap";

const PHOTO_API = "http://192.168.0.100:3000/public/";

type RouteProps = {
	routes: Route[]
}

export default function CallRoutes({ routes }: RouteProps) {
	return (
		<Container >
			<p>Number of routes: {routes.length}</p>
			<div className="row">
				{routes.map((route) => (
					<div className="col-12 col-sm-4 col-xl-3">
					<Card key={route.id} className="my-2 border border-dark border-2">
						<Card.Img src={PHOTO_API + route.photo}/>
						<Card.Body className="border-top border-2 border-dark">
							<Card.Title>{route.name}</Card.Title>
							<Card.Subtitle>{route.user}</Card.Subtitle>
							<Card.Text>
								{route.grade + " | " + route.angle + " degree"}
								<br />{route.desc}
							</Card.Text>
						</Card.Body>
					</Card>
					</div>
				))}
			</div>
		</Container>
	);
}
