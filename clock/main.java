public class Main extends Application {

    private Timer timer;

    @Override
    public void start(final Stage primaryStage){

        AnchorPane ap = new AnchorPane();

        ap.setPrefWidth(480);
        ap.setPrefHeight(320);
        ap.setStyle("-fx-background-color: rgba(2,4,12,0.95)");

        final Label clockLabel = new Label();
        
        timer = new Timer();
        timer.schedule(new ClockTask(new ClockUpdateListener() {
            @Override
            public void update(final String time) {

                Platform.runLater(new Runnable() {
                    @Override
                    public void run() {
                        clockLabel.setText(time);
                    }
                });
            }
        }), 0, 1000);

        clockLabel.setFont(Font.font("DS-Digital", 110));
        clockLabel.setTextFill(Paint.valueOf("#CCFFFF"));
        
        ap.getChildren().add(clockLabel);
        clockLabel.setAlignment(Pos.CENTER);

        AnchorPane.setLeftAnchor(clockLabel, 40.0);
        AnchorPane.setRightAnchor(clockLabel, 40.0);
        AnchorPane.setTopAnchor(clockLabel, 40.0);
        AnchorPane.setBottomAnchor(clockLabel, 40.0);

        clockLabel.setOnMouseClicked(new EventHandler<MouseEvent>() {
            @Override
            public void handle(MouseEvent event) {
                //发生点击事件则关闭程序
                primaryStage.close();
                Platform.exit();
            }
        });

        Scene scene = new Scene(ap);
        primaryStage.setTitle("Hello World");
        primaryStage.setScene(scene);
        primaryStage.setFullScreen(true);
        primaryStage.setWidth(480);
        primaryStage.setHeight(320);
        primaryStage.initStyle(StageStyle.UNDECORATED);
        primaryStage.setAlwaysOnTop(true);
        primaryStage.show();
    }


    public static void main(String[] args) {
        launch(args);
    }


}


class ClockTask extends TimerTask {

    private ClockUpdateListener listener;

    ClockTask(ClockUpdateListener listener) {
        this.listener = listener;
    }

    @Override
    public void run() {
        listener.update(getCurrentHourMinute());
    }


    private String getCurrentHourMinute() {
        Calendar cal = Calendar.getInstance();
        int hour = cal.get(Calendar.HOUR_OF_DAY);
        int minute = cal.get(Calendar.MINUTE);
        int second = cal.get(Calendar.SECOND);
        String displayHour = hour < 10 ? "0" + hour : ""+ hour;
        String displayMinute = minute < 10 ? "0" + minute : ""+ minute;
        String displaySecond = second < 10 ? "0" + second : ""+ second;
        return displayHour + ":" + displayMinute + ":" + displaySecond;
    }

}


interface ClockUpdateListener {
    void update(String time);
}
