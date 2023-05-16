using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class rotateObject : MonoBehaviour
{
    bool storValue1;

    private float timeElapsed = 0;
    public float roatationSpeed; 
    public Transform target1;
    public Transform target3;
    public Quaternion current;
    public Quaternion rotation;

    private Quaternion targetRotation;// = Quaternion.Euler(rotationVector);//transform.rotation * Quaternion.Euler(rotationVector);
    private Quaternion targetRotation2;// = Quaternion.Euler(zeroRotationVector);
    private Quaternion targetRotation3;// = Quaternion.Euler(negRotationVector);
    private Quaternion test_myQuaternion;// = {targetRotation,targetRotation2,targetRotation3,targetRotation2,targetRotation};

    // Start is called before the first frame update
    void Start()
    {

    }
    float lerpDuration = 1f;
    bool rotating;
    
    // Update is called once per frame
    void Update()
    {
        bool check = false;
        if(check)
        {
            StartCoroutine(RotateUp());
            check=false;
        }
        
        else
            StartCoroutine(RotateDown());
            check=true;
    }

    void rotateFOV()
    {
        
    }

    IEnumerator RotateUp()
    {
        Vector3 rotationVector = new Vector3(0, 45, 0);
        Vector3 negRotationVector = new Vector3(0,-45,0);
        float speed = 0.9f;

        Vector3 relativePos = target1.position - transform.position;
        Quaternion rotation = Quaternion.LookRotation(relativePos);
        
        Quaternion current = transform.localRotation;
        transform.localRotation = Quaternion.Slerp(current, rotation, Time.deltaTime * speed);


        yield return null;
    }
    
    IEnumerator RotateDown()
    {
        float speed = 0.8f;
        Vector3 relativePos2 = target3.position - target1.position;
        Quaternion rotation2 = Quaternion.LookRotation(relativePos2);

        Quaternion current2 = transform.localRotation;
        transform.localRotation = Quaternion.Slerp(rotation, current, Time.deltaTime * speed);

        yield return new WaitForSeconds(10);

    }



}

