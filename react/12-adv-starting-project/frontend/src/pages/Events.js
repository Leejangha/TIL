import { useLoaderData } from 'react-router-dom';

import EventsList from '../components/EventsList';

function EventsPage() {
  return <EventsList events={fetchedEvents} />;
}

export default EventsPage;
