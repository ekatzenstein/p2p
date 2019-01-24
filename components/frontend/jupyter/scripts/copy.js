let ncp = require('ncp').ncp;

ncp.limit = 16;

ncp('./dev/src/components/chart/', './js/src/components/chart', (err) => {
  if (err) {
    return console.error(err);
  }
  ncp('./dev/src/style.css', './js/src/components/style.css', (e) => {
    if (e) {
      console.log(e);
    }
    console.log(
      'src code successfuly copied to example folder for jupyter notebooks'
    );
  });
});
