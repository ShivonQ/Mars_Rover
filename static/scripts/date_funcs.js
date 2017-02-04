/**
 * Created by School on 2/4/2017.
 */
function tomorrow(current_date) {
    console.log('Today: ' + current_date);
    var tomorrow = current_date;
    tomorrow.setDate(tomorrow.getDate() + 1);
    console.log('new today: ' + tomorrow)
}
function yesterday(current_date) {
    console.log('today: ' + current_date);
    var yesterday = current_date;
    yesterday.setData(yesterday.getDate() - 1);
    console.log('new today: ' + yesterday)
}
