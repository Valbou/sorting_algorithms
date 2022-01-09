/// rustc -O main.rs -o ./sortalgo

mod app;

use app::App;

fn main() {
    let mut ui = App::new();
    ui.exec();
}
