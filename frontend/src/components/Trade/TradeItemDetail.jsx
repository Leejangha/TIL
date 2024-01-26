import { useSubmit } from 'react-router-dom';

import classes from './TradeItemDetail.module.css';

function TradeItemDetail({ trade }) {
  const submit = useSubmit();

  function startDeleteHandler() {
    const proceed = window.confirm('Are you sure?');

    if (proceed) {
      submit(null, { method: 'delete' });
    }
  }

  return (
    <article className={classes.trade}>
      <img src={trade.image} alt={trade.title} />
      <p>{trade.region}</p>
      <h1>{trade.title}</h1>
      <p>{trade.price}원</p>
      <p>{trade.isDirectTranscation ? '직거래' : '택배배송'}</p>
      <p>{trade.content}</p>
      <menu className={classes.actions}>
        <button onClick={startDeleteHandler}>Delete</button>
      </menu>
    </article>
  );
}

export default TradeItemDetail;