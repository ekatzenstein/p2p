let ncp = require('ncp').ncp;

ncp.limit = 16;

ncp('./src/components/chart/', './jupyter/js/src/components/chart', (err) => {
  if (err) {
    return console.error(err);
  }
  ncp('./src/style.css', './jupyter/js/src/components/style.css', (e) => {
    if (e) {
      console.log(e);
    }

    process.chdir('./jupyter');
    console.log(
      'src code successfuly copied to example folder for jupyter notebooks'
    );
  });
});
