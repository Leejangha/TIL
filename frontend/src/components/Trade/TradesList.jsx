import classes from './TradesList.module.css';
import TradeItem from './TradeItem';

function TradesList({ trades }) {
  return (
    <div className={classes.trades}>
      <ul className={classes.list}>
        {trades.map((trade) => (
          <li key={trade.id} className={classes.item}>
            <TradeItem trade={trade} />
            <TradeItem trade={trade} />
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TradesList;
