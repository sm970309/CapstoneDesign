package com.example.yeartube;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.widget.ProgressBar;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class LoadingScreenActivity extends AppCompatActivity {

    private TextView textView;
    private ProgressBar progressBar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_loading_screen);

        textView = findViewById(R.id.loading_text);
        progressBar = findViewById(R.id.progress_bar);

        // MainActivity에서 전달된 텍스트 가져오기
        String text = getIntent().getStringExtra("text");
        textView.setText(text);

        // 임시 함수 구현
        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                if (tempFunction()) {
                    // 새로운 액티비티를 시작하고 로딩 화면 종료
                    Intent intent = new Intent(LoadingScreenActivity.this, ResultActivity.class);
                    startActivity(intent);
                    finish();
                } else {
                    // tempFunction이 false를 반환하면 메인 화면으로 돌아감
                    finish();
                }


            }
        }, 3000);
    }
    @Override
    public void onBackPressed() {
        // 아무런 동작도 하지 않음
    }
    private boolean tempFunction() {
        // 임시 함수 구현
        return true;
    }
}
