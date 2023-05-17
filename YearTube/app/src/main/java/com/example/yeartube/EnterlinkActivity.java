package com.example.yeartube;

import static java.sql.DriverManager.println;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;


public class EnterlinkActivity extends AppCompatActivity {

    static RequestQueue requestQueue;
    Button btn_send_link;
    EditText edit_youtube_link;
    String text;
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.enterlink_activity);

        edit_youtube_link = (EditText) findViewById(R.id.edit_youtube_link);
        btn_send_link = (Button) findViewById(R.id.btn_send_link);
        //text = edit_youtube_link.getText().toString();
        text = "https://www.youtube.com/shorts/F8ECf8Vo_P0";
        String url = "https://267d-117-16-244-19.ngrok-free.app/";
        btn_send_link.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
                makeRequest();
            }
        });

        if (requestQueue == null) {
            requestQueue = Volley.newRequestQueue(getApplicationContext());
        }
    }
        public void makeRequest() {
            String url = edit_youtube_link.getText().toString();
            JSONObject jsonBodyObj = new JSONObject();
            try{
                jsonBodyObj.put("url",text);
            }catch (JSONException e){
                e.printStackTrace();
            }
            final String requestBody = String.valueOf(jsonBodyObj.toString());
            JsonObjectRequest request = new JsonObjectRequest(Request.Method.POST, "https://267d-117-16-244-19.ngrok-free.app/check/", jsonBodyObj,
                new Response.Listener<JSONObject>() {
                        @Override
                        public void onResponse(JSONObject response) {
                            System.out.println(response);
                            //여기서 response 다루기
                            try {
                                String result = response.getString("result");
                                if (result.equals("y")) {
                                    Intent intent = new Intent(getApplicationContext(), ResultActivity.class);
                                    String title = response.getString("title");
                                    int num_problem_sentences = response.getInt("num_problem_sentences");
                                    //int age = response.getInt("age");

                                    ArrayList<String> sentences = new ArrayList<String>();
                                    ArrayList<String> gpts = new ArrayList<String>();
                                    JSONArray jsentences = response.getJSONArray("problem_sentences");
                                    //JSONArray jgpts = response.getJSONArray("gpt");
                                    for (int i = 0; i < num_problem_sentences; i++) {
                                        Object element = jsentences.get(i);
                                        JSONObject arr = (JSONObject) element;
                                        sentences.add(arr.getString("sentence") + " : \n <" + arr.getString("reason") + ">\n");
                                        //gpts.add(arr.getString("gpt"));
                                    }

                                    intent.putStringArrayListExtra("problem_sentences", sentences);
                                    //intent.putStringArrayListExtra("gpts", gpts);
                                    intent.putExtra("title", title);
                                    ///intent.putExtra("age", age);
                                    intent.putExtra("num_problem_sentences", num_problem_sentences);
                                    startActivity(intent);
                                } else {
                                    Intent intent = new Intent(getApplicationContext(), MainActivity.class);
                                    startActivity(intent);
                                }
                            } catch (JSONException e) {
                                throw new RuntimeException(e);
                            }

                        }
                    },
                    new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {
                            //Log.e("error response",error.getMessage());

                        }
                    }
            );

            request.setShouldCache(false);
            requestQueue.add(request);

            request.setRetryPolicy(new com.android.volley.DefaultRetryPolicy(

                    60000 ,

                    com.android.volley.DefaultRetryPolicy.DEFAULT_MAX_RETRIES,

                    com.android.volley.DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
        }

}

