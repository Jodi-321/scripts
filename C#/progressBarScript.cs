using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class progressBar : MonoBehaviour
{
    private playerDeskCol pullScript;
    private gameOver gameOverScript;
    public GameObject holder;
    public GameObject playerTest;
    private Slider slider;

    public float FillSpeed = 0.1f;
    private float targetProgress = 0;

    private void Awake()
    {
        slider = gameObject.GetComponent<Slider>();
    }

    void Start()
    {
        pullScript = playerTest.GetComponent<playerDeskCol>();
        gameOverScript = holder.GetComponent<gameOver>();

    }

    void Update()
    {
        
        if(slider.value < targetProgress)
        {
            if(targetProgress > 1)
            {
                if(pullScript.playerCheck)
                {
                    Debug.Log("Game Win!");
                    
                    gameOverScript.sendGameWin();
                }
            }
            slider.value += FillSpeed * Time.deltaTime;
            Debug.Log(targetProgress);
        }
        
    }

    public void IncrementProgress(float newProgress)
    {
        targetProgress = slider.value + newProgress;
    }
}
